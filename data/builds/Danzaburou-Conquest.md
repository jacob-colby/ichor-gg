---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.37
    win_rate: 0.59
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.22
      win_rate: 0.6
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.53
  - name: Book of Thoth
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.65
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.58
  - name: Dagger of Frenzy
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: The World Stone
      pick_rate: 0.07
      win_rate: 0.4
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.5
  - name: The Executioner
    pick_rate: 0.14
    win_rate: 0.58
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.5
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.71
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.42
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.82
  - name: Time-lock Aegis
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.6
    - name: Killing Stone
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.25
    win_rate: 0.65
  - name: Death's Embrace
    pick_rate: 0.16
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-10-10'
  god_win_rate: 0.5766423357664233
  god_matches_won: 79
  god_matches_played: 137
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - The Crusher
  - Heartseeker
  flex_slots:
  - Transcendence
  - Book of Thoth
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean Bow, Tekko-Kagi,
    Tyrfing, The Reaper, Gluttonous Grimoire, Silverbranch Bow, Bragi''s Harp, Spear
    of the Magus, Deathbringer, Hydra''s Lament, Golden Blade, Spear of Desolation,
    Obsidian Shard, Demon Blade, Titan''s Bane, Bracer of The Abyss, Musashi''s Dual
    Swords, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound Book, Ancient Signet,
    Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s Idol, Qin''s Blade,
    Chronos'' Pendant, Pendulum Blade, Bancroft''s Talon, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.57
      pick: 0.27
      fit: 0.05
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.37
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.37
      fit: 0.18
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.43
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.53
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Crusher
  - Soul Gem
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation, Spear
    of the Magus, Hydra''s Lament, Obsidian Shard, Bragi''s Harp, Lernaean Bow, The
    Reaper, Tyrfing, Tekko-Kagi, Doom Orb, Ancient Signet, Riptalon, Bracer of The
    Abyss, Chronos'' Pendant, Silverbranch Bow, Deathbringer, Bancroft''s Talon, Titan''s
    Bane, Blood-Bound Book, Dreamer''s Idol, Golden Blade, Arondight, Gem of Focus,
    Musashi''s Dual Swords, Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Pendulum Blade, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.39
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.55
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.35
      fit: 0.35
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Demon Blade
  - The Crusher
  - Deathbringer
  - Heartseeker
  flex_slots:
  - Deathbringer
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
    this god: Death Metal, Nimble Ring, Soul Gem, Riptalon, Gluttonous Grimoire, Lernaean
    Bow, The Reaper, Tekko-Kagi, Tyrfing, Silverbranch Bow, Deathbringer, Spear of
    the Magus, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Demon Blade, Hydra''s
    Lament, Golden Blade, Musashi''s Dual Swords, Titan''s Bane, Bracer of The Abyss,
    Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound Book, Ancient Signet, Dreamer''s
    Idol, Chronos'' Pendant, Avatar''s Parashu, Runeforged Hammer, Arondight, Qin''s
    Blade, Bancroft''s Talon, Pendulum Blade, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.34
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.49
    Demon Blade:
      total: 0.5
      efficiency: 0.38
      win: 0.59
      pick: 0.0
      fit: 0.67
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.4
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.5
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    god: Soul Gem, Nimble Ring, Death Metal, Gluttonous Grimoire, Spear of Desolation,
    Spear of the Magus, Obsidian Shard, The Reaper, Riptalon, Tekko-Kagi, Silverbranch
    Bow, Hydra''s Lament, Lernaean Bow, Bragi''s Harp, Tyrfing, Doom Orb, Chronos''
    Pendant, Titan''s Bane, Bracer of The Abyss, Dreamer''s Idol, Deathbringer, Ancient
    Signet, Blood-Bound Book, Pendulum Blade, Golden Blade, Arondight, Gem of Focus,
    Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual Swords, The
    Cosmic Horror, Demon Blade, Runeforged Hammer, Rod of Asclepius, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.57
      pick: 0.27
      fit: 0.13
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.46
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.59
      pick: 0.37
      fit: 0.13
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.53
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.35
      fit: 0.33
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - The Crusher
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
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, The Reaper, Riptalon,
    Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius, Nimble Ring, Death
    Metal, Kinetic Cuirass, Runeforged Hammer, Golden Blade, Freya''s Tears, Genji''s
    Guard, Blood-Bound Book, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Lernaean Bow, Pharaoh''s
    Curse, Eye of the Storm, Tyrfing, Shogun''s Ofuda, Phoenix Feather, Spear of the
    Magus, Lifebinder, Silverbranch Bow, Tekko-Kagi, Erosion, Helm of Radiance, Hydra''s
    Lament, Eye of Providence, Daybreak Gavel, Toxic Blade, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.25
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.32
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    for this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Riptalon, Death Metal,
    The Reaper, Tekko-Kagi, Silverbranch Bow, Spear of the Magus, Obsidian Shard,
    Spear of Desolation, Titan''s Bane, Lernaean Bow, Tyrfing, Avenging Blade, Doom
    Orb, Toxic Blade, Hydra''s Lament, Dreamer''s Idol, Bragi''s Harp, Deathbringer,
    Avatar''s Parashu, Golden Blade, Pendulum Blade, Bracer of The Abyss, Demon Blade,
    Musashi''s Dual Swords, The Cosmic Horror, Oath-Sworn Spear, Ancient Signet, Blood-Bound
    Book, Runeforged Hammer, Chronos'' Pendant, Arondight, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.57
      pick: 0.27
      fit: 0.04
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.48
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.59
      pick: 0.37
      fit: 0.15
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.55
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.65
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Heartseeker
  flex_slots:
  - Tyrfing
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Riptalon, Tyrfing, Silverbranch Bow, Soul
    Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper,
    Spear of the Magus, Bragi''s Harp, Obsidian Shard, Spear of Desolation, Toxic
    Blade, Hydra''s Lament, Deathbringer, Bracer of The Abyss, Qin''s Blade, Demon
    Blade, Titan''s Bane, Musashi''s Dual Swords, Doom Orb, Ancient Signet, Blood-Bound
    Book, Chronos'' Pendant, Dreamer''s Idol, Sun Beam Bow, Runeforged Hammer, Arondight,
    Damaru, Bancroft''s Talon, Rage, Berserker''s Shield, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.28
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.59
      pick: 0.37
      fit: 0.13
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.59
      pick: 0.0
      fit: 0.62
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - The Crusher
  - Death Metal
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
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Spear of Desolation,
    Death Metal, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear of
    the Magus, Riptalon, Lernaean Bow, Obsidian Shard, Silverbranch Bow, The Reaper,
    Tyrfing, Arondight, Gem of Focus, Tekko-Kagi, Bragi''s Harp, Bracer of The Abyss,
    Pendulum Blade, Deathbringer, Doom Orb, Ancient Signet, Blood-Bound Book, Golden
    Blade, Titan''s Bane, Totem of Death, Dreamer''s Idol, Breastplate of Valor, Toxic
    Blade, Bancroft''s Talon, Musashi''s Dual Swords, Demon Blade, Genji''s Guard,
    Qin''s Blade, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.48
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.35
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.3
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.4
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Heartseeker
  - Soul Gem
  flex_slots:
  - The Crusher
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard, Bragi''s Harp,
    Lernaean Bow, The Reaper, Riptalon, Hydra''s Lament, Bracer of The Abyss, Chronos''
    Pendant, Tekko-Kagi, Silverbranch Bow, Tyrfing, Doom Orb, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Deathbringer, Gem of Focus, Titan''s Bane, Bancroft''s
    Talon, Golden Blade, Arondight, Rod of Asclepius, Musashi''s Dual Swords, The
    Cosmic Horror, Demon Blade, Toxic Blade, Polynomicon, Pendulum Blade, Typhon’s
    Heart, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.38
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.71
      pick: 0.17
      fit: 0.37
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.47
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Spear of the Magus, Obsidian Shard, Spear of Desolation,
    Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi, Riptalon, Tyrfing, Silverbranch
    Bow, Bracer of The Abyss, Hydra''s Lament, Doom Orb, Deathbringer, Titan''s Bane,
    Ancient Signet, Golden Blade, Dreamer''s Idol, Blood-Bound Book, Chronos'' Pendant,
    Demon Blade, Musashi''s Dual Swords, Bancroft''s Talon, Toxic Blade, Runeforged
    Hammer, Avatar''s Parashu, Arondight, Gem of Focus, The Cosmic Horror, Rod of
    Asclepius, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.57
      pick: 0.27
      fit: 0.18
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.36
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.59
      pick: 0.37
      fit: 0.18
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.82
      pick: 0.19
      fit: 0.53
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.35
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean
    Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire, Silverbranch Bow, Bragi''s
    Harp, Spear of the Magus, Deathbringer, Hydra''s Lament, Golden Blade, Spear of
    Desolation, Obsidian Shard, Demon Blade, Titan''s Bane, Bracer of The Abyss, Musashi''s
    Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, The World Stone, Blood-Bound
    Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s
    Idol, Qin''s Blade, Chronos'' Pendant, Pendulum Blade, Bancroft''s Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.16
      fit: 0.37
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.35
      fit: 0.2
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Rod of Tahuti
  starter: *id001
---
