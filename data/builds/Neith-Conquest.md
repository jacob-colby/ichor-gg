---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.79
  slot_order:
  - name: Tyrfing
    pick_rate: 0.32
    win_rate: 0.75
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.3
      win_rate: 0.45
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.25
  - name: Odysseus' Bow
    pick_rate: 0.24
    win_rate: 0.67
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.67
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.4
  - name: The World Stone
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.4
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 1.0
  - name: The Executioner
    pick_rate: 0.15
    win_rate: 1.0
    alternates:
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.0
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.75
  - name: Divine Ruin
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.13
      win_rate: 0.5
    - name: Survivor's Sash
      pick_rate: 0.13
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.63
  - name: Conduit Gem
    pick_rate: 0.19
    win_rate: 0.43
  - name: Death's Embrace
    pick_rate: 0.16
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-09-10'
  god_win_rate: 0.5945945945945946
  god_matches_won: 22
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s Harp, Tekko-Kagi, Hydra''s
    Lament, Bracer of The Abyss, Heartseeker, Doom Orb, Chronos'' Pendant, Deathbringer,
    Ancient Signet, Blood-Bound Book, Golden Blade, Titan''s Bane, Dominance, The
    Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade, Musashi''s Dual Swords,
    Gem of Focus, Arondight, Transcendence, Pendulum Blade, Rod of Asclepius, The
    Cosmic Horror, Runeforged Hammer, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    The Executioner:
      total: 0.64
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.3
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.49
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.49
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.41
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Hydra's Lament
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper,
    Tekko-Kagi, Doom Orb, Ancient Signet, Bracer of The Abyss, Chronos'' Pendant,
    Dominance, Deathbringer, Bancroft''s Talon, Titan''s Bane, Blood-Bound Book, The
    Crusher, Golden Blade, Transcendence, Arondight, Gem of Focus, Musashi''s Dual
    Swords, Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius, Soul Reaver,
    Pendulum Blade, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.26
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.38
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.35
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.32
  community_ordered:
  - The Executioner
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - The Executioner
  - Musashi's Dual Swords
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Lernaean Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s
    Lament, Heartseeker, Bracer of The Abyss, Deathbringer, Doom Orb, Chronos'' Pendant,
    Ancient Signet, Blood-Bound Book, Titan''s Bane, The Crusher, Golden Blade, Dominance,
    Musashi''s Dual Swords, Demon Blade, Bancroft''s Talon, Gem of Focus, Toxic Blade,
    Arondight, Transcendence, Damaru, Rage, Rod of Asclepius, Pendulum Blade, Book
    of Thoth.'
  slot_scores:
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.29
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.46
      win: 0.53
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.46
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.39
    Deathbringer:
      total: 0.47
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.36
  community_ordered:
  - The Executioner
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean
    Bow, Bragi''s Harp, Doom Orb, Chronos'' Pendant, Titan''s Bane, The Crusher, Bracer
    of The Abyss, Deathbringer, Ancient Signet, Blood-Bound Book, Pendulum Blade,
    Dominance, Golden Blade, Arondight, Gem of Focus, Toxic Blade, Bancroft''s Talon,
    Avatar''s Parashu, Musashi''s Dual Swords, The Cosmic Horror, Demon Blade, Transcendence,
    Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.46
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.27
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.45
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.33
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.41
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - The Executioner
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, The Reaper, Nimble Ring, Shield of the Phoenix, Death
    Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Bancroft''s Talon, Spear of the Magus, Runeforged Hammer,
    Yogi''s Necklace, Golden Blade, Lifebinder, Helm of Radiance, Shifter''s Shield,
    Sphere of Negation, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Chandra''s
    Grace, Phoenix Feather, Hydra''s Lament, Shogun''s Ofuda, Eye of the Storm, Daybreak
    Gavel, Heartseeker, Erosion.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.35
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.24
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.38
    Riptalon:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.64
    Silverbranch Bow:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.29
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.59
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire, Death
    Metal, Spear of the Magus, The Reaper, Tekko-Kagi, Heartseeker, Doom Orb, Lernaean
    Bow, Titan''s Bane, The Crusher, Bragi''s Harp, Hydra''s Lament, Avenging Blade,
    Bracer of The Abyss, Toxic Blade, Chronos'' Pendant, Ancient Signet, Deathbringer,
    Blood-Bound Book, The Cosmic Horror, Pendulum Blade, Avatar''s Parashu, Dominance,
    Golden Blade, Bancroft''s Talon, Gem of Focus, Musashi''s Dual Swords, Arondight,
    Demon Blade, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.45
    The Executioner:
      total: 0.68
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.57
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.43
    Riptalon:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.56
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.4
    Silverbranch Bow:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.49
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s Harp, Tekko-Kagi, Bracer
    of The Abyss, Hydra''s Lament, Golden Blade, Heartseeker, Doom Orb, Chronos''
    Pendant, Toxic Blade, Ancient Signet, Deathbringer, Dominance, Blood-Bound Book,
    Titan''s Bane, The Crusher, Qin''s Blade, Bancroft''s Talon, Gem of Focus, Demon
    Blade, Musashi''s Dual Swords, Arondight, Transcendence, Rod of Asclepius, Runeforged
    Hammer, Polynomicon, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.3
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.3
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.54
    Riptalon:
      total: 0.72
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.52
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.25
    Silverbranch Bow:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.46
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear
    of the Magus, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Heartseeker,
    Bragi''s Harp, Bracer of The Abyss, Pendulum Blade, Doom Orb, Deathbringer, Ancient
    Signet, Titan''s Bane, The Crusher, Dominance, Blood-Bound Book, Golden Blade,
    Totem of Death, Toxic Blade, Breastplate of Valor, Bancroft''s Talon, Musashi''s
    Dual Swords, Genji''s Guard, Demon Blade, Transcendence, Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.49
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.28
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.41
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.36
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.66
  community_ordered:
  - The Executioner
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul Gem,
    Death Metal, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Bracer of
    The Abyss, The Reaper, Lernaean Bow, Chronos'' Pendant, Hydra''s Lament, Doom
    Orb, Tekko-Kagi, Ancient Signet, Heartseeker, Blood-Bound Book, Gem of Focus,
    Deathbringer, Bancroft''s Talon, Titan''s Bane, The Crusher, Dominance, Golden
    Blade, Arondight, Rod of Asclepius, The Cosmic Horror, Toxic Blade, Polynomicon,
    Musashi''s Dual Swords, Typhon’s Heart, Demon Blade, Pendulum Blade, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.28
    Tyrfing:
      total: 0.59
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.44
    Riptalon:
      total: 0.7
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.44
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.35
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.37
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - The Executioner
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, Nimble
    Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, The Reaper,
    Lernaean Bow, Tekko-Kagi, Hydra''s Lament, Heartseeker, Bracer of The Abyss, Doom
    Orb, Deathbringer, Chronos'' Pendant, Titan''s Bane, Ancient Signet, The Crusher,
    Dominance, Golden Blade, Blood-Bound Book, Musashi''s Dual Swords, Bancroft''s
    Talon, Demon Blade, Arondight, Gem of Focus, Transcendence, Toxic Blade, Runeforged
    Hammer, Pendulum Blade, Avatar''s Parashu, Rod of Asclepius, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.39
    The Executioner:
      total: 0.63
      efficiency: 0.35
      win: 1.0
      pick: 0.32
      fit: 0.28
    Tyrfing:
      total: 0.6
      efficiency: 0.48
      win: 0.75
      pick: 0.32
      fit: 0.51
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.53
    Riptalon:
      total: 0.71
      efficiency: 0.51
      win: 1.0
      pick: 0.22
      fit: 0.45
    Silverbranch Bow:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.23
      fit: 0.38
  community_ordered:
  - The Executioner
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Gluttonous Grimoire, Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s Harp,
    Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Doom Orb, Chronos''
    Pendant, Deathbringer, Ancient Signet, Blood-Bound Book, Golden Blade, Titan''s
    Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade, Musashi''s
    Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum Blade, Rod of Asclepius,
    The Cosmic Horror, Book of Thoth, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.45
      pick: 0.3
      fit: 0.38
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.32
      fit: 0.3
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
