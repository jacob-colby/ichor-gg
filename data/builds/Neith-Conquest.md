---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.42
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.29
    win_rate: 0.63
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.44
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.47
  - name: Book of Thoth
    pick_rate: 0.14
    win_rate: 0.69
    alternates:
    - name: The World Stone
      pick_rate: 0.13
      win_rate: 0.67
    - name: Dagger of Frenzy
      pick_rate: 0.1
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.75
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.67
    - name: Silverbranch Bow
      pick_rate: 0.14
      win_rate: 0.58
  - name: Ancient Signet
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.57
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.67
  - name: Dreamer's Idol
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.16
      win_rate: 0.89
    - name: Riptalon
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.29
    win_rate: 0.7
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.44
  - name: Pendulum of the Ages
    pick_rate: 0.09
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-11-06'
  god_win_rate: 0.5483870967741935
  god_matches_won: 51
  god_matches_played: 93
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Death Metal
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  flex_slots:
  - Death Metal
  - Nimble Ring
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
    this god: Death Metal, Soul Gem, Jotunn''s Revenge, Nimble Ring, Tyrfing, Gluttonous
    Grimoire, Bragi''s Harp, The Reaper, Blood-Bound Book, Tekko-Kagi, Spear of the
    Magus, Hydra''s Lament, Bracer of The Abyss, The Crusher, Polynomicon, Chronos''
    Pendant, Lernaean Bow, Dominance, Heartseeker, Doom Orb, Titan''s Bane, Bancroft''s
    Talon, Arondight, Golden Blade, Toxic Blade, Soul Reaver, Gem of Focus, Heartwood
    Charm, Rage, Demon Blade, Qin''s Blade, Deathbringer, The Cosmic Horror, Ancient
    Signet.'
  slot_scores:
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.38
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.3
    Riptalon:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.49
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.3
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Death Metal
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Jotunn''s Revenge, Soul Gem, Tyrfing, Nimble Ring, Bragi''s Harp, Hydra''s
    Lament, Gluttonous Grimoire, The Reaper, Blood-Bound Book, Polynomicon, Heartseeker,
    Dominance, Tekko-Kagi, Spear of the Magus, Chronos'' Pendant, The Crusher, Bracer
    of The Abyss, Lernaean Bow, Doom Orb, Bancroft''s Talon, Heartwood Charm, Soul
    Reaver, Titan''s Bane, Arondight, Gem of Focus, Golden Blade, Rage, Ancient Signet,
    Transcendence, Deathbringer, Avatar''s Parashu, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.35
    Riptalon:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.38
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.29
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Death Metal
  - Riptalon
  - Deathbringer
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Rage
  - Deathbringer
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
    this god: Death Metal, Soul Gem, Jotunn''s Revenge, Nimble Ring, Gluttonous Grimoire,
    Tyrfing, The Reaper, Bragi''s Harp, Blood-Bound Book, Spear of the Magus, Tekko-Kagi,
    Hydra''s Lament, Bracer of The Abyss, The Crusher, Polynomicon, Chronos'' Pendant,
    Heartseeker, Lernaean Bow, Dominance, Doom Orb, Titan''s Bane, Bancroft''s Talon,
    Rage, Arondight, Soul Reaver, Gem of Focus, Golden Blade, Heartwood Charm, Toxic
    Blade, Deathbringer, Demon Blade, Qin''s Blade, The Cosmic Horror, Ancient Signet.'
  slot_scores:
    Rage:
      total: 0.49
      efficiency: 0.46
      win: 0.6
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.46
    Deathbringer:
      total: 0.48
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.3
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.3
  community_ordered:
  - Riptalon
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
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
    god: Soul Gem, Jotunn''s Revenge, Death Metal, Gluttonous Grimoire, The Reaper,
    Tyrfing, Nimble Ring, Hydra''s Lament, Tekko-Kagi, Bragi''s Harp, Spear of the
    Magus, Blood-Bound Book, The Crusher, Heartseeker, Chronos'' Pendant, Titan''s
    Bane, Polynomicon, Bracer of The Abyss, Doom Orb, Lernaean Bow, Dominance, Arondight,
    Gem of Focus, Heartwood Charm, Toxic Blade, Bancroft''s Talon, Golden Blade, Avatar''s
    Parashu, Soul Reaver, Rage, Pendulum Blade, The Cosmic Horror, Deathbringer, Ancient
    Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.13
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.46
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.33
    Riptalon:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.48
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  - Dreamer's Idol
  - Amanita Charm
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
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
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Blood-Bound Book, Shield
    of the Phoenix, The Reaper, Gluttonous Grimoire, Kinetic Cuirass, Genji''s Guard,
    Death Metal, Jotunn''s Revenge, Ethereal Staff, Yogi''s Necklace, Phoenix Feather,
    Bancroft''s Talon, Freya''s Tears, Nimble Ring, Breastplate of Valor, Tyrfing,
    Shield Splitter, Chandra''s Grace, Oni Hunter''s Garb, Runeforged Hammer, Golden
    Blade, Helm of Radiance, Bragi''s Harp, Sphere of Negation, Regrowth Striders,
    Hydra''s Lament, Draconic Scale, Bloodforge, Spear of the Magus, Polynomicon,
    Midgardian Mail, Erosion, Shogun''s Ofuda, Ancient Signet.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.27
    Riptalon:
      total: 0.71
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.64
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.21
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.21
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
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
    for this god: Soul Gem, Jotunn''s Revenge, Death Metal, Gluttonous Grimoire, The
    Reaper, Spear of the Magus, Tekko-Kagi, Nimble Ring, Tyrfing, The Crusher, Heartseeker,
    Blood-Bound Book, Bragi''s Harp, Titan''s Bane, Doom Orb, Hydra''s Lament, Polynomicon,
    Bracer of The Abyss, Chronos'' Pendant, Toxic Blade, Lernaean Bow, Dominance,
    Avenging Blade, The Cosmic Horror, Avatar''s Parashu, Bancroft''s Talon, Arondight,
    Soul Reaver, Gem of Focus, Golden Blade, Heartwood Charm, Pendulum Blade, Rage,
    Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.13
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.47
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.4
    Riptalon:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.56
    Dreamer's Idol:
      total: 0.59
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.4
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  flex_slots:
  - Tyrfing
  - Nimble Ring
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
    this god: Death Metal, Soul Gem, Jotunn''s Revenge, Tyrfing, Nimble Ring, Gluttonous
    Grimoire, Bragi''s Harp, The Reaper, Blood-Bound Book, Tekko-Kagi, Hydra''s Lament,
    Spear of the Magus, Bracer of The Abyss, Polynomicon, The Crusher, Chronos'' Pendant,
    Lernaean Bow, Dominance, Golden Blade, Heartseeker, Toxic Blade, Qin''s Blade,
    Titan''s Bane, Doom Orb, Bancroft''s Talon, Arondight, Soul Reaver, Gem of Focus,
    Heartwood Charm, Rage, Demon Blade, Deathbringer, Ancient Signet, Dagger of Frenzy.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.54
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.32
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.25
    Riptalon:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.52
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.25
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Death
    Metal, Hydra''s Lament, Chronos'' Pendant, Tyrfing, Nimble Ring, Gluttonous Grimoire,
    The Reaper, Arondight, Blood-Bound Book, Bragi''s Harp, Gem of Focus, Heartwood
    Charm, Tekko-Kagi, Spear of the Magus, The Crusher, Bracer of The Abyss, Polynomicon,
    Lernaean Bow, Heartseeker, Dominance, Damaru, Genji''s Guard, Titan''s Bane, Totem
    of Death, Pendulum Blade, Doom Orb, Toxic Blade, Bancroft''s Talon, Golden Blade,
    Soul Reaver, Qin''s Blade, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.08
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.49
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.21
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.21
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  flex_slots:
  - Death Metal
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Soul Gem, Death Metal, Jotunn''s Revenge,
    Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, Blood-Bound Book, Tyrfing, The
    Reaper, Spear of the Magus, Chronos'' Pendant, Bracer of The Abyss, Polynomicon,
    Hydra''s Lament, Tekko-Kagi, The Crusher, Doom Orb, Heartseeker, Gem of Focus,
    Lernaean Bow, Heartwood Charm, Dominance, Bancroft''s Talon, Soul Reaver, Titan''s
    Bane, Arondight, The Cosmic Horror, Golden Blade, Toxic Blade, Ancient Signet,
    Rage, Totem of Death, Typhon’s Heart, Qin''s Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.21
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.46
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.35
    Riptalon:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.44
    Dreamer's Idol:
      total: 0.58
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Soul Gem, Jotunn''s Revenge,
    Tyrfing, Nimble Ring, Gluttonous Grimoire, Bragi''s Harp, The Reaper, Blood-Bound
    Book, Tekko-Kagi, Hydra''s Lament, Spear of the Magus, The Crusher, Bracer of
    The Abyss, Polynomicon, Heartseeker, Lernaean Bow, Dominance, Chronos'' Pendant,
    Titan''s Bane, Doom Orb, Arondight, Bancroft''s Talon, Golden Blade, Soul Reaver,
    Rage, Gem of Focus, Heartwood Charm, Toxic Blade, Deathbringer, Demon Blade, Avatar''s
    Parashu, The Cosmic Horror, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.17
    Death Metal:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.39
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.31
    Riptalon:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.15
      fit: 0.45
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.54
      win: 0.71
      pick: 0.4
      fit: 0.31
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Riptalon
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Death Metal, Soul Gem, Jotunn''s Revenge, Nimble Ring,
    Tyrfing, Gluttonous Grimoire, Bragi''s Harp, The Reaper, Blood-Bound Book, Tekko-Kagi,
    Spear of the Magus, Hydra''s Lament, Ancient Signet, Bracer of The Abyss, The
    Crusher, Polynomicon, Chronos'' Pendant, Lernaean Bow, Dominance, Heartseeker,
    Doom Orb, Titan''s Bane, Bancroft''s Talon, Arondight, Golden Blade, Toxic Blade,
    Soul Reaver, Gem of Focus, Heartwood Charm, Rage, Demon Blade, Qin''s Blade, Deathbringer,
    The Cosmic Horror.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.29
      fit: 0.38
    Nimble Ring:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.82
      win: 0.69
      pick: 0.28
      fit: 0.3
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
