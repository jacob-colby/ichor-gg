---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.57
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.25
    win_rate: 0.8
    alternates:
    - name: Book of Thoth
      pick_rate: 0.25
      win_rate: 0.6
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 1.0
  - name: Spear of Desolation
    pick_rate: 0.2
    win_rate: 0.75
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.15
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.67
    - name: Rod of Asclepius
      pick_rate: 0.11
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.05
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Nimble Ring
      pick_rate: 0.19
      win_rate: 0.67
    - name: Manchu Bow
      pick_rate: 0.13
      win_rate: 1.0
  - name: Manchu Bow
    pick_rate: 0.3
    win_rate: 1.0
    alternates:
    - name: Medallion
      pick_rate: 0.1
      win_rate: 1.0
    - name: Adroit Ring
      pick_rate: 0.1
      win_rate: 0.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.2
    win_rate: 0.5
  - name: Pendulum of the Ages
    pick_rate: 0.2
    win_rate: 0.75
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-09-09'
  god_win_rate: 0.65
  god_matches_won: 13
  god_matches_played: 20
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer
    of The Abyss, The World Stone, Chronos'' Pendant, Dreamer''s Idol, Blood-Bound
    Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Typhon’s
    Heart, Polynomicon, Totem of Death, Soul Reaver, Bragi''s Harp, Jade Scepter,
    Divine Ruin, Helm of Radiance, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.24
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.12
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.56
    Nimble Ring:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.68
    Doom Orb:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.44
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.44
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Doom
    Orb, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Ancient
    Signet, The World Stone, Bracer of The Abyss, Death Metal, Chronos'' Pendant,
    Bancroft''s Talon, Blood-Bound Book, Dreamer''s Idol, Gem of Focus, Polynomicon,
    Soul Reaver, The Cosmic Horror, Typhon’s Heart, Totem of Death, Jade Scepter,
    Divine Ruin, Triton''s Conch, Wish-Granting Pearl.'
  slot_scores:
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.18
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.45
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.48
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.42
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.42
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.44
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Doom Orb, Breastplate of Valor, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Bragi''s Harp, The World Stone, Chronos'' Pendant, Bracer of The Abyss,
    Dreamer''s Idol, Death Metal, Ancient Signet, Blood-Bound Book, Gem of Focus,
    The Cosmic Horror, Bancroft''s Talon, Totem of Death, Typhon’s Heart, Polynomicon,
    Soul Reaver, Jade Scepter, Divine Ruin.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.16
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.16
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.56
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.44
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.4
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.4
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Shield of the Phoenix, Kinetic Cuirass, Blood-Bound Book, Freya''s Tears, Bancroft''s
    Talon, Spear of the Magus, Shifter''s Shield, Lifebinder, Helm of Radiance, Yogi''s
    Necklace, Sphere of Negation, Phoenix Feather, Erosion, Eye of Providence, Jade
    Scepter, Bracer of The Abyss, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.71
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.19
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.34
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.42
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.27
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.27
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Spear of the Magus, The
    World Stone, Dreamer''s Idol, Bracer of The Abyss, The Cosmic Horror, Chronos''
    Pendant, Blood-Bound Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, Typhon’s
    Heart, Polynomicon, Soul Reaver, Totem of Death, Jade Scepter, Divine Ruin, Screeching
    Gargoyle, Helm of Radiance, Bragi''s Harp.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.09
    Spear of Desolation:
      total: 0.65
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.66
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.53
    Doom Orb:
      total: 0.72
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.57
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.57
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.67
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Chronos'' Pendant, Ancient Signet, The World Stone,
    Blood-Bound Book, Death Metal, Dreamer''s Idol, Bancroft''s Talon, Gem of Focus,
    The Cosmic Horror, Typhon’s Heart, Polynomicon, Soul Reaver, Jade Scepter, Totem
    of Death, Divine Ruin, Helm of Radiance, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.08
    Bracer of The Abyss:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.49
    Bragi's Harp:
      total: 0.55
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.64
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.3
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.3
  community_ordered:
  - Breastplate of Valor
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Doom Orb, Breastplate of Valor, Soul
    Gem, Gluttonous Grimoire, Chronos'' Pendant, Spear of the Magus, Gem of Focus,
    Bragi''s Harp, Bracer of The Abyss, Totem of Death, The World Stone, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Death Metal, Bancroft''s Talon, The Cosmic
    Horror, Typhon’s Heart, Polynomicon, Staff of Myrddin, Eye of Erebus, Soul Reaver.'
  slot_scores:
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.34
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.59
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.24
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.24
    Soul Gem:
      total: 0.62
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Doom Orb, Jotunn''s Revenge, Soul Gem, Gluttonous
    Grimoire, The Reaper, Tyrfing, Spear of the Magus, Heartseeker, Riptalon, Hydra''s
    Lament, Tekko-Kagi, Bragi''s Harp, Lernaean Bow, Silverbranch Bow, Titan''s Bane,
    Death Metal, The Crusher, Golden Blade, The World Stone, Chronos'' Pendant, Pendulum
    Blade, Dreamer''s Idol, Arondight, Dominance, Blood-Bound Book, Avatar''s Parashu,
    Ancient Signet, Bracer of The Abyss, Transcendence, Toxic Blade, Runeforged Hammer,
    Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Avenging Blade, Barbed Carver.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.2
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.59
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.29
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.41
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.39
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Doom Orb, Jotunn''s Revenge, Soul
    Gem, Gluttonous Grimoire, Riptalon, Tyrfing, Spear of the Magus, Bragi''s Harp,
    Silverbranch Bow, Tekko-Kagi, The Reaper, Lernaean Bow, Golden Blade, Heartseeker,
    Hydra''s Lament, Bracer of The Abyss, Death Metal, The World Stone, Titan''s Bane,
    Dominance, The Crusher, Chronos'' Pendant, Toxic Blade, Dreamer''s Idol, Ancient
    Signet, Blood-Bound Book, Bancroft''s Talon, Arondight, Gem of Focus, Pendulum
    Blade, Qin''s Blade, Avatar''s Parashu, Transcendence, The Cosmic Horror, Runeforged
    Hammer, Typhon’s Heart.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.09
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.47
    Nimble Ring:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.53
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.39
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Spear of Desolation
  - Nimble Ring
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer
    of The Abyss, Doom Orb, The World Stone, Chronos'' Pendant, Dreamer''s Idol, Blood-Bound
    Book, Ancient Signet, Bancroft''s Talon, Gem of Focus, The Cosmic Horror, Typhon’s
    Heart, Polynomicon, Totem of Death, Soul Reaver, Bragi''s Harp, Jade Scepter,
    Divine Ruin, Helm of Radiance, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.56
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.56
    Nimble Ring:
      total: 0.65
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.68
    Spear of the Magus:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.44
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.54
  community_ordered:
  - Spear of Desolation
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Amanita Charm, Spear of the
    Magus, Void Stone, Bracer of The Abyss, Doublet of Binding, Lifebinder, Chronos''
    Pendant, Screeching Gargoyle, The World Stone, Blood-Bound Book, Dreamer''s Idol,
    Jade Scepter, Ancient Signet, Gem of Focus, Wish-Granting Pearl, Bancroft''s Talon,
    Freya''s Tears, Erosion, Ancile.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.12
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.17
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.46
    Nimble Ring:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.5
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.29
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.29
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Doom
    Orb, Soul Gem, Gluttonous Grimoire, Triton''s Conch, Spear of the Magus, Amanita
    Charm, Bragi''s Harp, Lifebinder, Ancient Signet, The World Stone, Bracer of The
    Abyss, Death Metal, Void Stone, Chronos'' Pendant, Wish-Granting Pearl, Doublet
    of Binding, Bancroft''s Talon, Blood-Bound Book, Jade Scepter, Dreamer''s Idol,
    Gem of Focus, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.16
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.21
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.4
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.37
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.37
    Soul Gem:
      total: 0.63
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Doom Orb, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Amanita Charm,
    Triton''s Conch, Bragi''s Harp, Void Stone, Lifebinder, Chronos'' Pendant, The
    World Stone, Bracer of The Abyss, Doublet of Binding, Dreamer''s Idol, Screeching
    Gargoyle, Ancient Signet, Death Metal, Blood-Bound Book, Jade Scepter, Gem of
    Focus, Wish-Granting Pearl, Daybreak Gavel, Bancroft''s Talon.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.6
      pick: 0.25
      fit: 0.14
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.14
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.49
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.39
    Doom Orb:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.35
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Spear of Desolation
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Shield of the Phoenix, Lifebinder, Erosion, Kinetic Cuirass, Freya''s Tears, Umbral
    Link, Void Shield, Stampede, Void Stone, Spectral Armor, Blood-Bound Book, Doublet
    of Binding, Shifter''s Shield, Bancroft''s Talon, Yogi''s Necklace, Spear of the
    Magus, Helm of Radiance, Phoenix Feather.'
  slot_scores:
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.65
      win: 1.0
      pick: 0.14
      fit: 0.24
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.33
    Doom Orb:
      total: 0.67
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.21
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.21
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.99
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Void Stone
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Void Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Void Stone, Spear of the
    Magus, Screeching Gargoyle, Amanita Charm, The World Stone, Dreamer''s Idol, Doublet
    of Binding, Lifebinder, Bracer of The Abyss, Chronos'' Pendant, The Cosmic Horror,
    Ancient Signet, Blood-Bound Book, Jade Scepter, Wish-Granting Pearl, Gem of Focus,
    Bancroft''s Talon, Freya''s Tears, Erosion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.13
    Void Stone:
      total: 0.59
      efficiency: 0.45
      win: 0.67
      pick: 0.0
      fit: 0.83
    Spear of Desolation:
      total: 0.64
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.57
    Doom Orb:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.43
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.43
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Doom Orb
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Doom Orb, Soul Gem, Gluttonous Grimoire, Amanita Charm, Spear of the
    Magus, Triton''s Conch, Void Stone, Bragi''s Harp, Doublet of Binding, Bracer
    of The Abyss, Lifebinder, Chronos'' Pendant, Screeching Gargoyle, Daybreak Gavel,
    Ancient Signet, The World Stone, Blood-Bound Book, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Dreamer''s Idol, Gem of Focus, Bancroft''s Talon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.12
    Bracer of The Abyss:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.41
      fit: 0.38
    Bragi's Harp:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.53
    Doom Orb:
      total: 0.67
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.21
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.21
  community_ordered:
  - Breastplate of Valor
  - Nimble Ring
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Doom Orb, Soul Gem, Gluttonous Grimoire,
    Amanita Charm, Chronos'' Pendant, Screeching Gargoyle, Spear of the Magus, Void
    Stone, Triton''s Conch, Gem of Focus, Doublet of Binding, Lifebinder, Bragi''s
    Harp, Freya''s Tears, Bracer of The Abyss, Eye of Erebus, Daybreak Gavel, Ancient
    Signet, Totem of Death, The World Stone, Blood-Bound Book, Jade Scepter.'
  slot_scores:
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.3
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.36
    Spear of Desolation:
      total: 0.63
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.52
    Doom Orb:
      total: 0.67
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.21
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.21
    Soul Gem:
      total: 0.65
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.99
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - Shogun's Ofuda
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Shogun''s Ofuda, Doom Orb, Jotunn''s Revenge,
    Soul Gem, Gluttonous Grimoire, Golden Blade, The Reaper, Hydra''s Lament, Triton''s
    Conch, Runeforged Hammer, Sanguine Lash, Tyrfing, Pharaoh''s Curse, Amanita Charm,
    Heartseeker, Riptalon, Spear of the Magus, Tekko-Kagi, Lernaean Bow, Silverbranch
    Bow, Titan''s Bane, The Crusher, Bragi''s Harp, Eye of the Storm, Void Stone,
    Avenging Blade, Toxic Blade, Arondight, Doublet of Binding, Death Metal, Pendulum
    Blade, Lifebinder, Chronos'' Pendant, Dominance, Screeching Gargoyle, Transcendence.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.14
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.41
    Doom Orb:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.28
    Shogun's Ofuda:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.08
      fit: 0.54
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Breastplate of Valor
  - Spear of Desolation
  - Doom Orb
  - Shogun's Ofuda
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Doom Orb
  - Rod of Tahuti
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shogun''s Ofuda, Doom Orb, Soul Gem,
    Jotunn''s Revenge, Gluttonous Grimoire, Pharaoh''s Curse, Golden Blade, Triton''s
    Conch, Spear of the Magus, Riptalon, Tyrfing, Amanita Charm, Silverbranch Bow,
    Bragi''s Harp, The Reaper, Lernaean Bow, Hydra''s Lament, Tekko-Kagi, Runeforged
    Hammer, Sanguine Lash, Heartseeker, Toxic Blade, Lifebinder, Bracer of The Abyss,
    Void Stone, Chronos'' Pendant, Death Metal, Eros'' Bow, Doublet of Binding, The
    World Stone, Titan''s Bane, Ancient Signet, The Crusher, Dominance, Dreamer''s
    Idol, Blood-Bound Book.'
  slot_scores:
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.47
      win: 1.0
      pick: 0.14
      fit: 0.12
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.44
    Doom Orb:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.1
      fit: 0.32
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.32
    Shogun's Ofuda:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.08
      fit: 0.61
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Breastplate of Valor
  - Doom Orb
  - Rod of Tahuti
  - Shogun's Ofuda
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Spear of Desolation
  - Genji's Guard
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Spear of
    the Magus, Void Stone, Bracer of The Abyss, Doublet of Binding, Lifebinder, Chronos''
    Pendant, Screeching Gargoyle, Doom Orb, The World Stone, Blood-Bound Book, Dreamer''s
    Idol, Jade Scepter, Ancient Signet, Gem of Focus, Wish-Granting Pearl, Bancroft''s
    Talon, Freya''s Tears, Erosion, Ancile.'
  slot_scores:
    Spear of Desolation:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.27
      fit: 0.46
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.25
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.29
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.86
      win: 0.67
      pick: 0.41
      fit: 0.29
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.27
      fit: 0.39
    Soul Gem:
      total: 0.64
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spear of Desolation
  - Genji's Guard
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
  aspect: Aspect of Relativity
---
