---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.83
  slot_order:
  - name: Transcendence
    pick_rate: 0.4
    win_rate: 0.47
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.19
      win_rate: 0.44
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.58
  - name: Book of Thoth
    pick_rate: 0.15
    win_rate: 0.69
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.3
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.13
    win_rate: 0.36
    alternates:
    - name: Polynomicon
      pick_rate: 0.1
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.57
  - name: Nimble Ring
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.44
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.75
  - name: Rod of Tahuti
    pick_rate: 0.24
    win_rate: 0.61
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.5
    - name: Polynomicon
      pick_rate: 0.05
      win_rate: 0.75
  - name: Evil Eye
    pick_rate: 0.08
    win_rate: 0.25
    alternates:
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.33
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.64
  - name: Conduit Gem
    pick_rate: 0.16
    win_rate: 0.57
  - name: Leather Cowl
    pick_rate: 0.13
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-11-06'
  god_win_rate: 0.4823529411764706
  god_matches_won: 41
  god_matches_played: 85
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
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Transcendence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Tyrfing, Soul Gem, The Reaper, Tekko-Kagi, Bragi''s Harp,
    Spear of Desolation, Gluttonous Grimoire, Lernaean Bow, The Crusher, Hydra''s
    Lament, Heartseeker, Riptalon, Blood-Bound Book, Obsidian Shard, Titan''s Bane,
    Golden Blade, Bracer of The Abyss, Demon Blade, Rage, Spear of the Magus, Ancient
    Signet, Toxic Blade, Deathbringer, Dreamer''s Idol, Arondight, Qin''s Blade, Avatar''s
    Parashu, Chronos'' Pendant, Doom Orb, Bancroft''s Talon, The World Stone, Bloodforge,
    Runeforged Hammer.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.05
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.18
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.48
    Nimble Ring:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.39
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.2
    Silverbranch Bow:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.24
      fit: 0.45
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    Metal, Soul Gem, Spear of Desolation, Tyrfing, Bragi''s Harp, Hydra''s Lament,
    Gluttonous Grimoire, The Reaper, Ancient Signet, Blood-Bound Book, Obsidian Shard,
    Heartseeker, Tekko-Kagi, Spear of the Magus, Chronos'' Pendant, The Crusher, Bracer
    of The Abyss, Lernaean Bow, Dreamer''s Idol, Doom Orb, Bancroft''s Talon, Heartwood
    Charm, Soul Reaver, The World Stone, Titan''s Bane, Arondight, Gem of Focus, Golden
    Blade, Rage, Riptalon, Deathbringer, Avatar''s Parashu, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.24
    Transcendence:
      total: 0.44
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.24
    Hydra's Lament:
      total: 0.45
      efficiency: 0.55
      win: 0.44
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.51
    Nimble Ring:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.4
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Book of Thoth
  - Rage
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Demon Blade
  flex_slots:
  - Rage
  - Demon Blade
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Soul Gem, Tyrfing, The Reaper, Tekko-Kagi, Spear of Desolation,
    Gluttonous Grimoire, Bragi''s Harp, The Crusher, Lernaean Bow, Riptalon, Blood-Bound
    Book, Hydra''s Lament, Heartseeker, Obsidian Shard, Titan''s Bane, Rage, Demon
    Blade, Spear of the Magus, Bracer of The Abyss, Golden Blade, Ancient Signet,
    Deathbringer, Dreamer''s Idol, Toxic Blade, Arondight, Qin''s Blade, Chronos''
    Pendant, Doom Orb, Avatar''s Parashu, Bancroft''s Talon, The World Stone, Bloodforge,
    Soul Reaver, Musashi''s Dual Swords.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.05
    Rage:
      total: 0.43
      efficiency: 0.46
      win: 0.44
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.38
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.2
    Demon Blade:
      total: 0.43
      efficiency: 0.36
      win: 0.44
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Book of Thoth
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Spear of Desolation
  flex_slots:
  - Spear of Desolation
  - Transcendence
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
    god: Soul Gem, Death Metal, Spear of Desolation, Gluttonous Grimoire, The Reaper,
    Tyrfing, Obsidian Shard, Hydra''s Lament, Tekko-Kagi, Bragi''s Harp, Spear of
    the Magus, Blood-Bound Book, The Crusher, Heartseeker, Dreamer''s Idol, Chronos''
    Pendant, Ancient Signet, Titan''s Bane, Bracer of The Abyss, Doom Orb, Riptalon,
    Lernaean Bow, Arondight, The World Stone, Gem of Focus, Heartwood Charm, Toxic
    Blade, Bancroft''s Talon, Avatar''s Parashu, Soul Reaver, Golden Blade, Rage,
    Pendulum Blade, The Cosmic Horror, Deathbringer.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.13
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.13
    Death Metal:
      total: 0.48
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.37
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.33
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, The Reaper, Shield of
    the Phoenix, Kinetic Cuirass, Blood-Bound Book, Genji''s Guard, Death Metal, Gluttonous
    Grimoire, Yogi''s Necklace, Phoenix Feather, Riptalon, Shield Splitter, Tyrfing,
    Ethereal Staff, Freya''s Tears, Golden Blade, Runeforged Hammer, Bancroft''s Talon,
    Oni Hunter''s Garb, Breastplate of Valor, Chandra''s Grace, Draconic Scale, Spear
    of Desolation, Bloodforge, Shogun''s Ofuda, Hydra''s Lament, Tekko-Kagi, Pharaoh''s
    Curse, Erosion, Bragi''s Harp, Midgardian Mail, Eye of Providence, Toxic Blade,
    Regrowth Striders, The Crusher, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.03
    Berserker's Shield:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.42
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.12
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.26
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.14
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Death Metal
  - Transcendence
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, The Reaper, Death Metal, Tekko-Kagi, Spear of Desolation,
    Gluttonous Grimoire, Tyrfing, The Crusher, Heartseeker, Obsidian Shard, Titan''s
    Bane, Riptalon, Spear of the Magus, Dreamer''s Idol, Bragi''s Harp, Toxic Blade,
    Hydra''s Lament, Lernaean Bow, Blood-Bound Book, Doom Orb, Avatar''s Parashu,
    Avenging Blade, The World Stone, Ancient Signet, Bracer of The Abyss, Golden Blade,
    Rage, Arondight, Pendulum Blade, The Cosmic Horror, Demon Blade, Chronos'' Pendant,
    Deathbringer, Qin''s Blade, Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.04
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.15
    Death Metal:
      total: 0.48
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.39
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.32
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.35
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.24
      fit: 0.55
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Transcendence
  - Tyrfing
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Transcendence
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
    this god: Tyrfing, Death Metal, Soul Gem, The Reaper, Riptalon, Tekko-Kagi, Bragi''s
    Harp, Spear of Desolation, Gluttonous Grimoire, Golden Blade, Lernaean Bow, Blood-Bound
    Book, The Crusher, Hydra''s Lament, Toxic Blade, Obsidian Shard, Qin''s Blade,
    Heartseeker, Bracer of The Abyss, Ancient Signet, Spear of the Magus, Titan''s
    Bane, Dreamer''s Idol, Demon Blade, Rage, Chronos'' Pendant, Arondight, Dagger
    of Frenzy, Deathbringer, Doom Orb, Bancroft''s Talon, The World Stone, Avatar''s
    Parashu, Berserker''s Shield, Soul Reaver.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.04
    Transcendence:
      total: 0.42
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.13
    Tyrfing:
      total: 0.48
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.62
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.36
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.17
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.24
      fit: 0.52
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Transcendence
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Soul Gem, Spear of Desolation, Death
    Metal, Hydra''s Lament, Chronos'' Pendant, Tyrfing, Gluttonous Grimoire, Arondight,
    The Reaper, Blood-Bound Book, Bragi''s Harp, Gem of Focus, Heartwood Charm, Obsidian
    Shard, Ancient Signet, Tekko-Kagi, Spear of the Magus, Bracer of The Abyss, The
    Crusher, Lernaean Bow, Damaru, Genji''s Guard, Heartseeker, Dreamer''s Idol, Riptalon,
    Totem of Death, Titan''s Bane, Pendulum Blade, Doom Orb, Bancroft''s Talon, Golden
    Blade, Toxic Blade, Soul Reaver, The World Stone, Rage.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.08
    Transcendence:
      total: 0.42
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.08
    Hydra's Lament:
      total: 0.46
      efficiency: 0.55
      win: 0.44
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.2
    Soul Gem:
      total: 0.5
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Spear of Desolation
  flex_slots:
  - Spear of Desolation
  - Transcendence
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
    + win/pick). Underrated for this god: Soul Gem, Death Metal, Spear of Desolation,
    Gluttonous Grimoire, Bragi''s Harp, Tyrfing, Blood-Bound Book, Obsidian Shard,
    The Reaper, Spear of the Magus, Ancient Signet, Chronos'' Pendant, Hydra''s Lament,
    Bracer of The Abyss, Dreamer''s Idol, Tekko-Kagi, The Crusher, Doom Orb, Heartseeker,
    Lernaean Bow, Gem of Focus, Heartwood Charm, The World Stone, Bancroft''s Talon,
    Titan''s Bane, Soul Reaver, Arondight, Riptalon, Golden Blade, The Cosmic Horror,
    Rage, Toxic Blade, Totem of Death, Typhon’s Heart, Deathbringer.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.2
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.13
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.51
    Nimble Ring:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.34
    Spear of Desolation:
      total: 0.48
      efficiency: 0.6
      win: 0.44
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Death Metal, Soul Gem, Tyrfing, Spear
    of Desolation, Bragi''s Harp, Gluttonous Grimoire, The Reaper, Blood-Bound Book,
    Obsidian Shard, Tekko-Kagi, Spear of the Magus, Ancient Signet, The Crusher, Bracer
    of The Abyss, Hydra''s Lament, Heartseeker, Dreamer''s Idol, Lernaean Bow, Titan''s
    Bane, Chronos'' Pendant, Doom Orb, Riptalon, The World Stone, Bancroft''s Talon,
    Golden Blade, Rage, Soul Reaver, Arondight, Demon Blade, Deathbringer, Toxic Blade,
    Avatar''s Parashu, Gem of Focus, Heartwood Charm, The Cosmic Horror.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.69
      pick: 0.2
      fit: 0.18
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.47
      pick: 0.4
      fit: 0.18
    Death Metal:
      total: 0.5
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.55
    Nimble Ring:
      total: 0.56
      efficiency: 0.57
      win: 0.64
      pick: 0.23
      fit: 0.45
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.82
      win: 0.61
      pick: 0.52
      fit: 0.33
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.24
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Rod of Tahuti
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Reaper
  - Tekko-Kagi
  - Soul Gem
  flex_slots:
  - The Reaper
  - Tekko-Kagi
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Death Metal, Tyrfing, Soul Gem, The Reaper, Tekko-Kagi,
    Bragi''s Harp, Spear of Desolation, Gluttonous Grimoire, Lernaean Bow, The Crusher,
    Hydra''s Lament, Heartseeker, Riptalon, Blood-Bound Book, Obsidian Shard, Titan''s
    Bane, Golden Blade, Bracer of The Abyss, Demon Blade, Rage, Spear of the Magus,
    Ancient Signet, Toxic Blade, Deathbringer, Dreamer''s Idol, Arondight, Qin''s
    Blade, Avatar''s Parashu, Chronos'' Pendant, Doom Orb, Bancroft''s Talon, The
    World Stone, Bloodforge, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.65
      win: 0.3
      pick: 0.16
      fit: 0.37
    Tyrfing:
      total: 0.47
      efficiency: 0.53
      win: 0.44
      pick: 0.0
      fit: 0.58
    Death Metal:
      total: 0.49
      efficiency: 0.63
      win: 0.44
      pick: 0.0
      fit: 0.48
    The Reaper:
      total: 0.46
      efficiency: 0.57
      win: 0.44
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.46
      efficiency: 0.49
      win: 0.44
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.47
      efficiency: 0.58
      win: 0.44
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
