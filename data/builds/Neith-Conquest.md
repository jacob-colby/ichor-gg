---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.64
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.34
    win_rate: 0.49
    alternates:
    - name: Tyrfing
      pick_rate: 0.21
      win_rate: 0.68
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.33
  - name: The World Stone
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.19
      win_rate: 0.5
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.52
  - name: Rod of Tahuti
    pick_rate: 0.23
    win_rate: 0.49
    alternates:
    - name: The World Stone
      pick_rate: 0.17
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.9
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.44
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.57
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.82
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.36
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.57
  - name: Killing Stone
    pick_rate: 0.09
    win_rate: 0.86
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.29
    - name: Dreamer's Idol
      pick_rate: 0.08
      win_rate: 0.17
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.29
    win_rate: 0.51
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.49
  - name: Death's Embrace
    pick_rate: 0.1
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-09-12'
  god_win_rate: 0.5466666666666666
  god_matches_won: 82
  god_matches_played: 150
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Death Metal
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Riptalon, Silverbranch Bow, Jotunn''s Revenge, Nimble Ring, Death Metal,
    Soul Gem, Gluttonous Grimoire, Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Doom Orb,
    Chronos'' Pendant, Deathbringer, Ancient Signet, Blood-Bound Book, Golden Blade,
    Titan''s Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade,
    Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum Blade,
    Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.49
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.41
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
  community_ordered:
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
  - Tyrfing
  - Hydra's Lament
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Riptalon,
    Silverbranch Bow, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous
    Grimoire, Spear of the Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, Heartseeker,
    The Reaper, Tekko-Kagi, Doom Orb, Ancient Signet, Bracer of The Abyss, Chronos''
    Pendant, Dominance, Deathbringer, Bancroft''s Talon, Titan''s Bane, Blood-Bound
    Book, The Crusher, Golden Blade, Transcendence, Arondight, Gem of Focus, Musashi''s
    Dual Swords, Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius, Soul
    Reaver, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.48
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.49
      pick: 0.36
      fit: 0.35
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.38
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.32
  community_ordered:
  - Tyrfing
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Death Metal
  - Musashi's Dual Swords
  - Riptalon
  - Silverbranch Bow
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Riptalon, Silverbranch Bow, Jotunn''s Revenge, Death Metal, Nimble Ring,
    Soul Gem, Gluttonous Grimoire, Spear of the Magus, The Reaper, Lernaean Bow, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Heartseeker, Bracer of The Abyss, Deathbringer,
    Doom Orb, Chronos'' Pendant, Ancient Signet, Blood-Bound Book, Titan''s Bane,
    The Crusher, Golden Blade, Dominance, Musashi''s Dual Swords, Demon Blade, Bancroft''s
    Talon, Gem of Focus, Toxic Blade, Arondight, Transcendence, Damaru, Rage, Rod
    of Asclepius, Pendulum Blade.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.46
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Musashi's Dual Swords:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.46
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.39
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    god: Riptalon, Silverbranch Bow, Jotunn''s Revenge, Soul Gem, Nimble Ring, Death
    Metal, Gluttonous Grimoire, Spear of the Magus, The Reaper, Tekko-Kagi, Hydra''s
    Lament, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb, Chronos'' Pendant,
    Titan''s Bane, The Crusher, Bracer of The Abyss, Deathbringer, Ancient Signet,
    Blood-Bound Book, Pendulum Blade, Dominance, Golden Blade, Arondight, Gem of Focus,
    Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual Swords, The
    Cosmic Horror, Demon Blade, Transcendence, Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.52
      pick: 0.2
      fit: 0.13
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.45
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.49
      pick: 0.36
      fit: 0.33
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.48
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Tyrfing
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Riptalon, Silverbranch Bow, Amanita Charm, Soul Gem, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, Rod of Asclepius, The Reaper, Nimble Ring,
    Shield of the Phoenix, Death Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal
    Staff, Genji''s Guard, Breastplate of Valor, Freya''s Tears, Bancroft''s Talon,
    Spear of the Magus, Runeforged Hammer, Yogi''s Necklace, Golden Blade, Lifebinder,
    Helm of Radiance, Shifter''s Shield, Sphere of Negation, Shield Splitter, Lernaean
    Bow, Pharaoh''s Curse, Chandra''s Grace, Phoenix Feather, Hydra''s Lament, Shogun''s
    Ofuda, Eye of the Storm, Daybreak Gavel, Heartseeker, Erosion.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.26
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.38
    Riptalon:
      total: 0.69
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.64
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.29
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Riptalon, Silverbranch Bow, Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Gluttonous Grimoire, Death Metal, Spear of the Magus, The Reaper, Tekko-Kagi,
    Heartseeker, Doom Orb, Lernaean Bow, Titan''s Bane, The Crusher, Bragi''s Harp,
    Hydra''s Lament, Avenging Blade, Bracer of The Abyss, Toxic Blade, Chronos'' Pendant,
    Ancient Signet, Deathbringer, Blood-Bound Book, The Cosmic Horror, Pendulum Blade,
    Avatar''s Parashu, Dominance, Golden Blade, The Executioner, Bancroft''s Talon,
    Gem of Focus, Musashi''s Dual Swords, Arondight, Demon Blade, Oath-Sworn Spear.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.52
      pick: 0.2
      fit: 0.13
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.49
      pick: 0.36
      fit: 0.4
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.56
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.49
  community_ordered:
  - Book of Thoth
  - Tyrfing
  - Rod of Tahuti
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Death Metal
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Riptalon, Silverbranch Bow, Jotunn''s Revenge, Nimble Ring, Death Metal,
    Soul Gem, Gluttonous Grimoire, Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Bracer of The Abyss, Hydra''s Lament, Golden Blade, Heartseeker,
    Doom Orb, Chronos'' Pendant, Toxic Blade, Ancient Signet, Deathbringer, Dominance,
    Blood-Bound Book, Titan''s Bane, The Crusher, Qin''s Blade, Bancroft''s Talon,
    Gem of Focus, Demon Blade, Musashi''s Dual Swords, Arondight, Transcendence, Rod
    of Asclepius, Runeforged Hammer, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.54
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.67
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.52
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.46
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Riptalon, Silverbranch Bow, Jotunn''s
    Revenge, Soul Gem, Nimble Ring, Death Metal, Hydra''s Lament, Gluttonous Grimoire,
    Chronos'' Pendant, Spear of the Magus, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight,
    Gem of Focus, Heartseeker, Bragi''s Harp, Bracer of The Abyss, Pendulum Blade,
    Doom Orb, Deathbringer, Ancient Signet, Titan''s Bane, The Crusher, Dominance,
    Blood-Bound Book, Golden Blade, Totem of Death, Toxic Blade, Breastplate of Valor,
    Bancroft''s Talon, Musashi''s Dual Swords, Genji''s Guard, Demon Blade, Transcendence,
    Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.41
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.34
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.49
      pick: 0.36
      fit: 0.21
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.36
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + win/pick). Underrated for this god: Riptalon, Silverbranch Bow, Jotunn''s Revenge,
    Nimble Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, The Reaper, Lernaean Bow, Chronos'' Pendant, Hydra''s
    Lament, Doom Orb, Tekko-Kagi, Ancient Signet, Heartseeker, Blood-Bound Book, Gem
    of Focus, Deathbringer, Bancroft''s Talon, Titan''s Bane, The Crusher, Dominance,
    Golden Blade, Arondight, Rod of Asclepius, The Cosmic Horror, Toxic Blade, Polynomicon,
    Musashi''s Dual Swords, Typhon’s Heart, Demon Blade, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.34
      fit: 0.46
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.65
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.44
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.37
  community_ordered:
  - Tyrfing
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Riptalon, Silverbranch Bow, Jotunn''s
    Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi, Hydra''s Lament, Heartseeker,
    Bracer of The Abyss, Doom Orb, Deathbringer, Chronos'' Pendant, Titan''s Bane,
    Ancient Signet, The Crusher, Dominance, Golden Blade, Blood-Bound Book, Musashi''s
    Dual Swords, Bancroft''s Talon, Demon Blade, Arondight, Gem of Focus, Transcendence,
    Toxic Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.21
      fit: 0.51
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.34
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.53
    Riptalon:
      total: 0.66
      efficiency: 0.51
      win: 0.9
      pick: 0.11
      fit: 0.45
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.82
      pick: 0.13
      fit: 0.38
  community_ordered:
  - Tyrfing
  - Spear of Desolation
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
    Gluttonous Grimoire, Spear of the Magus, Riptalon, Lernaean Bow, The Reaper, Silverbranch
    Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker,
    Doom Orb, Chronos'' Pendant, Deathbringer, Ancient Signet, Blood-Bound Book, Golden
    Blade, Titan''s Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon,
    Toxic Blade, Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum
    Blade, Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.34
      fit: 0.38
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.49
      pick: 0.36
      fit: 0.3
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
