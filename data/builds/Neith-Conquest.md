---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.67
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.27
    win_rate: 0.75
    alternates:
    - name: Tyrfing
      pick_rate: 0.23
      win_rate: 0.71
    - name: Spear of Desolation
      pick_rate: 0.2
      win_rate: 0.33
  - name: The World Stone
    pick_rate: 0.17
    win_rate: 0.4
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.17
      win_rate: 0.8
    - name: Chronos' Pendant
      pick_rate: 0.13
      win_rate: 0.75
  - name: Chronos' Pendant
    pick_rate: 0.19
    win_rate: 0.6
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.15
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.4
    alternates:
    - name: The World Stone
      pick_rate: 0.15
      win_rate: 0.5
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.12
    win_rate: 0.33
    alternates:
    - name: Dominance
      pick_rate: 0.08
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.08
      win_rate: 1.0
  - name: Hunter's Bow
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Ring of Dispel
      pick_rate: 0.13
      win_rate: 0.5
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.23
    win_rate: 0.86
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.33
  - name: Conduit Gem
    pick_rate: 0.2
    win_rate: 0.83
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-08-26'
  god_win_rate: 0.5666666666666667
  god_matches_won: 17
  god_matches_played: 30
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Rod of Tahuti
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
    Spear of the Magus, Riptalon, Lernaean Bow, The Reaper, Silverbranch Bow, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Doom Orb,
    Deathbringer, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Golden Blade,
    Titan''s Bane, The Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade, Musashi''s
    Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum Blade, Rod of Asclepius,
    The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.15
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.49
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.38
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.26
      fit: 0.3
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Chronos' Pendant
  - Rod of Tahuti
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
    Tekko-Kagi, Doom Orb, Ancient Signet, Riptalon, Bracer of The Abyss, Silverbranch
    Bow, Deathbringer, Bancroft''s Talon, Titan''s Bane, Blood-Bound Book, The Crusher,
    Golden Blade, Dreamer''s Idol, Transcendence, Arondight, Gem of Focus, Musashi''s
    Dual Swords, Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius, Soul
    Reaver, Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.24
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.3
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.48
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.38
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.26
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Book of Thoth
  - Tyrfing
  - Death Metal
  - Spear of Desolation
  - Musashi's Dual Swords
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
    Spear of the Magus, Riptalon, The Reaper, Lernaean Bow, Silverbranch Bow, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Heartseeker, Bracer of The Abyss, Deathbringer,
    Doom Orb, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Titan''s Bane, The
    Crusher, Golden Blade, Musashi''s Dual Swords, Demon Blade, Bancroft''s Talon,
    Gem of Focus, Toxic Blade, Arondight, Transcendence, Damaru, Rage, Rod of Asclepius,
    Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.15
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.46
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.38
    Musashi's Dual Swords:
      total: 0.44
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.36
    Deathbringer:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Chronos' Pendant
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
    Spear of the Magus, The Reaper, Riptalon, Silverbranch Bow, Tekko-Kagi, Hydra''s
    Lament, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb, Titan''s Bane, The
    Crusher, Bracer of The Abyss, Dreamer''s Idol, Deathbringer, Ancient Signet, Blood-Bound
    Book, Pendulum Blade, Golden Blade, Arondight, Gem of Focus, Toxic Blade, Bancroft''s
    Talon, Avatar''s Parashu, Musashi''s Dual Swords, The Cosmic Horror, Demon Blade,
    Transcendence, Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.13
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.3
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.45
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.46
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Tyrfing
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Berserker's Shield
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
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, Riptalon, The Reaper, Nimble Ring, Shield of the Phoenix,
    Death Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Bancroft''s Talon, Spear of the Magus, Runeforged
    Hammer, Yogi''s Necklace, Golden Blade, Lifebinder, Helm of Radiance, Shifter''s
    Shield, Sphere of Negation, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Chandra''s
    Grace, Phoenix Feather, Hydra''s Lament, Silverbranch Bow, Shogun''s Ofuda, Eye
    of the Storm, Daybreak Gavel, Heartseeker, Erosion.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.11
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.38
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.27
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Odysseus' Bow
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Odysseus' Bow
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
    Metal, Spear of the Magus, Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi,
    Heartseeker, Doom Orb, Lernaean Bow, Dreamer''s Idol, Titan''s Bane, The Crusher,
    Bragi''s Harp, Hydra''s Lament, Avenging Blade, Bracer of The Abyss, Toxic Blade,
    Ancient Signet, Deathbringer, Blood-Bound Book, The Cosmic Horror, Pendulum Blade,
    Avatar''s Parashu, Golden Blade, Bancroft''s Talon, Gem of Focus, Musashi''s Dual
    Swords, Arondight, Demon Blade, Oath-Sworn Spear.'
  slot_scores:
    Odysseus' Bow:
      total: 0.51
      efficiency: 0.34
      win: 0.75
      pick: 0.23
      fit: 0.27
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.13
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.43
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.47
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Odysseus' Bow
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  flex_slots:
  - Odysseus' Bow
  - Nimble Ring
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
    Riptalon, Silverbranch Bow, Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Bracer of The Abyss, Hydra''s Lament, Golden Blade, Heartseeker,
    Doom Orb, Toxic Blade, Ancient Signet, Deathbringer, Blood-Bound Book, Dreamer''s
    Idol, Titan''s Bane, The Crusher, Qin''s Blade, Bancroft''s Talon, Gem of Focus,
    Demon Blade, Musashi''s Dual Swords, Arondight, Transcendence, Rod of Asclepius,
    Runeforged Hammer, Polynomicon.'
  slot_scores:
    Odysseus' Bow:
      total: 0.51
      efficiency: 0.34
      win: 0.75
      pick: 0.23
      fit: 0.3
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.13
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.54
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Chronos' Pendant
  - Jotunn's Revenge
  - Tyrfing
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Soul Gem
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
    Ring, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Spear of the Magus, Riptalon,
    Silverbranch Bow, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus,
    Heartseeker, Bragi''s Harp, Bracer of The Abyss, Pendulum Blade, Doom Orb, Deathbringer,
    Ancient Signet, Titan''s Bane, The Crusher, Blood-Bound Book, Golden Blade, Dreamer''s
    Idol, Totem of Death, Toxic Blade, Breastplate of Valor, Bancroft''s Talon, Musashi''s
    Dual Swords, Genji''s Guard, Demon Blade, Transcendence, Qin''s Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.08
    Chronos' Pendant:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.3
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.56
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.41
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.49
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Rod of Tahuti
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
    Death Metal, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Riptalon,
    Bracer of The Abyss, The Reaper, Lernaean Bow, Silverbranch Bow, Hydra''s Lament,
    Doom Orb, Tekko-Kagi, Ancient Signet, Heartseeker, Blood-Bound Book, Dreamer''s
    Idol, Gem of Focus, Deathbringer, Bancroft''s Talon, Titan''s Bane, The Crusher,
    Golden Blade, Arondight, Rod of Asclepius, The Cosmic Horror, Toxic Blade, Polynomicon,
    Musashi''s Dual Swords, Typhon’s Heart, Demon Blade, Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.56
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.21
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.44
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.46
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.26
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Rod of Tahuti
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
    Lernaean Bow, Tekko-Kagi, Riptalon, Hydra''s Lament, Heartseeker, Silverbranch
    Bow, Bracer of The Abyss, Doom Orb, Deathbringer, Titan''s Bane, Ancient Signet,
    The Crusher, Golden Blade, Dreamer''s Idol, Blood-Bound Book, Musashi''s Dual
    Swords, Bancroft''s Talon, Demon Blade, Arondight, Gem of Focus, Transcendence,
    Toxic Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.55
      efficiency: 0.51
      win: 0.75
      pick: 0.27
      fit: 0.17
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.58
      efficiency: 0.48
      win: 0.71
      pick: 0.23
      fit: 0.51
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.39
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.26
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
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
    Doom Orb, Deathbringer, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Golden
    Blade, Titan''s Bane, The Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade,
    Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum Blade,
    Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
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
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.8
      pick: 0.23
      fit: 0.38
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.33
      pick: 0.26
      fit: 0.3
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
---
